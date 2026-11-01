"""Fictional shared cases, generated once and checked by both runtimes."""
import copy
import importlib.util
import json
import sys
from pathlib import Path
from typing import get_args

root = Path(__file__).resolve().parents[2]
spec = importlib.util.spec_from_file_location('schema_contract', root/'pydantic/__init__.py', submodule_search_locations=[str(root/'pydantic')])
pkg = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = pkg
spec.loader.exec_module(pkg)
from schema_contract import sourced_entities as e
from schema_contract import sourced_entities_vocabulary as v

citation = {'source_id':'fictional-source','page':'1'}
fact = dict(id='fictional-fact', type='occupation', value='Fictional trade', citations=[citation], evidence_confidence='confirmed', identity_confidence='confirmed', status='accepted', review={'state':'pending'}, attribution={'by':'fixture','on':'2024-02-29'})
person = dict(id='fictional-person', name='Fictional Person', names=[], gender='unknown')
archive = json.loads((root/'tests/contract/site-shapes.fixtures.json').read_text(encoding='utf-8'))['example']
bases = dict(SourcedDate={'start':'1940'}, Review={'state':'pending'}, Attribution={'by':'fixture','on':'2024-02-29'}, Source={'id':'fictional-source','kind':'book','title':'Fictional source'}, Citation=citation, Fact=fact, Name={'value':'Fictional Person','kind':'printed','script':'Latn'}, Fate={'outcome':'unknown','confidence':'possible','rests_on':[],'review':{'state':'pending'}}, Mention={'id':'fictional-mention','person_id':'fictional-person','unit_id':'fictional-unit','printed_name':'Fictional Person'}, SharedPerson=person, SiteArchive=archive)
models = {name:getattr(pkg,name) for name in bases}
cases=[]
def add(name, model, value, valid=True):
    cases.append(dict(name=name,model=model,value=copy.deepcopy(value),valid=valid))
def change(model, name, valid=False, **updates):
    add(name,model,dict(bases[model],**updates),valid)

for model, base in bases.items():
    add('baseline '+model,model,base)
    for name, field in models[model].model_fields.items():
        # Optional fields retain their omission/null behavior in the current carrier.
        if not field.is_required():
            optional_base = copy.deepcopy(base)
            if model == 'SourcedDate': optional_base['printed'] = 'Fictional printed date'
            if model == 'Fact': optional_base.update(type='office')
            if model == 'Citation': optional_base['unit_id'] = 'fictional-unit'
            optional_base.pop(name, None)
            add(f'{model}.{name} omitted',model,optional_base)
            add(f'{model}.{name} null',model,dict(optional_base,**{name:None}))
    change(model,model+' unknown key',unexpected=True)

# Non-null examples exercise all optional field shapes as well as omission/null.
change('SourcedDate','all date fields',True,start='1940-02-01',end='1940-02-29',precision='range',printed='Fictional date',printed_calendar='hebrew',inferred=True)
change('Review','review metadata',True,by='fixture',on='2024-02-29')
change('Attribution','attribution note',True,note='Fictional note')
change('Source','all source metadata',True,**{n:'Fictional metadata' for n in 'work_id author editor published repository url_pattern short_name holder_id reference_code'.split()},host='fictional.example.org')
change('Source','host with a scheme',False,host='https://fictional.example.org')
change('Source','host with www',False,host='www.fictional.example.org')
change('Source','host in capitals',False,host='Fictional.example.org')
change('Source','host with no dot',False,host='localhost')
change('Citation','all citation metadata',True,record_id='fictional-record',scan='1',time='00:01',edition_date='1938-01-01',unit_id='fictional-unit',url='https://example.org/fictional',quote='Fictional quote',quote_language='en',note='Private fictional remark',accessed='2024-02-29')
change('Citation','non-English quote without English is refused',quote='Fiktive verter.',quote_language='yi-Latn')
change('Fact','all fact payload shapes',True,date={'start':'1940'},place_id='fictional-place',organization_id='fictional-org',event_id='fictional-event',related_person_id='fictional-relative',relationship_type='child_of',related_name='Fictional Relative',qualifiers={'fictional':'value'},holocaust_related=False)
change('Name','name citations',True,lang='en',citations=[citation])
change('Fate','fate summary',True,summary='Fictional summary')
change('Mention','mention metadata',True,role='named',title='Fictional title',function='Fictional function',wkd_id='fictional-id')

for model, field, enum in [('Fact','type',v.FactTypes),('Fact','relationship_type',v.RelationshipTypes),('Fact','evidence_confidence',v.Confidence),('Fact','identity_confidence',v.Confidence),('Fact','status',v.ClaimStatus),('Name','kind',v.NameKinds),('Mention','role',v.MentionRoles),('Source','kind',v.SourceKinds),('Review','state',v.ReviewStates),('Fate','outcome',v.FateOutcomes),('Fate','confidence',v.Confidence)]:
    for value in get_args(enum):
        data=dict(bases[model],**{field:value})
        if model=='Fact':
            data.update(event_id='fictional-event',relationship_type=data.get('relationship_type','child_of'),related_name='Fictional Relative')
            if value=='other': data['proposed_type']='fictional proposal'
        if model=='Review' and value=='approved': data.update(by='fixture',on='2024-02-29')
        if model=='Fate': data['rests_on']=['fictional-fact']
        if model=='Name' and value=='supplied': data.update(attribution=bases['Attribution'],citations=[citation])
        add(f'{model}.{field}={value}',model,data)
    change(model,f'{model}.{field} invalid',**{field:'invented'})

for value, valid in [({'start':'1940-02-29','precision':'day'},True),({'start':'1900-02-29'},False),({'start':'2000-02-29'},True),({'start':'0000'},False),({'start':'1940-13'},False),({'start':'1940-04-31'},False),({'start':'1939-05','end':'1939','precision':'range'},True),({'start':'1940','end':'1939-12','precision':'range'},False),({'start':'1940-02','precision':'month'},True),({'start':'1940','precision':'year'},True),({'start':'1940','precision':'day'},False),({'start':'1940','precision':'range'},False),({'end':'1940'},False),({},False),({'printed':'Fictional Hebrew date','printed_calendar':'hebrew'},True),({'printed':'Fictional date','printed_calendar':'gregorian'},True),({'start':'1940','printed_calendar':'hebrew'},False)]:
    add('date '+repr(value),'SourcedDate',value,valid)
for model, field in [('Review','on'),('Attribution','on'),('Citation','accessed')]:
    change(model,model+' invalid day',**{field:'2023-02-29'})
change('Review','approval missing reviewer',state='approved',on='2024-02-29')
change('Review','approval blank reviewer',state='approved',by=' ',on='2024-02-29')
change('Review','approval missing day',state='approved',by='fixture')
for key in ['record_id','page','scan','time','unit_id','url','locator','reference_code']:
    add('locator '+key,'Citation',dict(source_id='fictional-source',**{key:'https://example.org/fictional' if key=='url' else '1'}))
    add('empty locator '+key,'Citation',dict(source_id='fictional-source',**{key:' '}),False)
for data in [{'source_id':'fictional-source'},{'source_id':'fictional-source','edition_date':'1938-01-01','quote':'Fictional quote'}]: add('no locator '+repr(data),'Citation',data,False)
change('Citation','http URL',url='http://example.org/fictional')
for kind, required in [('occupation',{}),('residence',{}),('event_participation',{}),('birth',{}),('death',{}),('kinship',{}),('kinship',{'relationship_type':'child_of'}),('kinship',{'related_name':'Fictional Relative'}),('other',{})]:
    data=dict(fact,type=kind,**required);data.pop('value',None);add('missing payload '+kind+repr(required),'Fact',data,False)
for kind, payloads in [('birth',[{'date':{'start':'1940'}},{'place_id':'fictional-place'},{'value':'Fictional birth'}]),('death',[{'date':{'start':'1940'}},{'place_id':'fictional-place'},{'value':'Fictional death'}]),('residence',[{'place_id':'fictional-place'},{'value':'Fictional residence'}]),('kinship',[{'relationship_type':'child_of','related_person_id':'fictional-relative'},{'relationship_type':'child_of','related_name':'Fictional Relative'}])]:
    for payload in payloads:
        data=dict(fact,type=kind);data.pop('value');data.update(payload);add('payload '+kind+repr(payload),'Fact',data)
change('Fact','proposed type forbidden',proposed_type='fictional')
change('Fact','blank proposed type',type='other',proposed_type=' ')
change('Fact','empty citations',citations=[])
change('Name','invalid script',script='Latin')
change('Name','invalid lang',lang='en_XX')
change('Name','BCP shaped lang',True,lang='zh-Hant-TW',script='Cyrl')
change('Name','supplied name needs attribution',kind='supplied',citations=[citation])
change('Name','supplied name needs citations',kind='supplied',attribution=bases['Attribution'])
change('Name','supplied name refuses empty citations',kind='supplied',attribution=bases['Attribution'],citations=[])
change('Name','supplied attribution cannot label printed words',attribution=bases['Attribution'],citations=[citation])
change('Name','supplied cannot use the old proposed spelling',kind='other',proposed_type='supplied',attribution=bases['Attribution'],citations=[citation])
change('Fate','left_before forbidden',outcome='left_before',rests_on=['fictional-fact'])
change('Fate','known without facts',outcome='survived')
full=copy.deepcopy(archive)
record=full['shared_record']
record['sources']=[bases['Source'],*(s for s in record['sources'] if s['id']!=bases['Source']['id'])]
record['facts']=[dict(fact, subject_id=person['id'], representation='structured')]
record['persons'][0].update(names=[dict(bases['Name'],citations=[citation])],fate=dict(bases['Fate'],outcome='survived',rests_on=['fictional-fact']))
add('complete archive','SiteArchive',full)
for label, mutate in [
    ('unknown fact source', lambda d:d['shared_record']['facts'][0]['citations'][0].update(source_id='missing')),
    ('unknown name source', lambda d:d['shared_record']['persons'][0]['names'][0]['citations'][0].update(source_id='missing')),
    ('missing sources', lambda d:d['shared_record'].pop('sources')),
    ('unknown mention person', lambda d:d['issues'][0]['mentions']['mentions'][0].update(person_id='missing')),
    ('foreign fate fact', lambda d:d['shared_record']['persons'][0]['fate'].update(rests_on=['foreign-fact'])),
]:
    data=copy.deepcopy(full);mutate(data);add(label,'SiteArchive',data,False)
data=copy.deepcopy(full)
data['shared_record']['persons'].append(dict(person,id='fictional-other'))
data['shared_record']['facts'].append(dict(fact,id='foreign-fact',subject_id='fictional-other',representation='structured'))
data['shared_record']['persons'][0]['fate']['rests_on']=['foreign-fact']
add('fate cannot rest on another person facts','SiteArchive',data,False)
# Shared exhaustive mapping expectations, independent of either helper.
legacy=[]
for outcome in get_args(v.FateOutcomes):
    for confidence in get_args(v.Confidence):
        value=dict(bases['Fate'],outcome=outcome,confidence=confidence,rests_on=['fictional-fact'])
        expected=('likely_'+outcome if confidence!='confirmed' else outcome) if outcome in ('perished','survived') else outcome
        assert e.legacyHolocaustFate(e.Fate.model_validate(value))==expected
        legacy.append(dict(value=value,expected=expected))
for case in cases:
    # The current carrier contains strict geometry tuples: validate its JSON wire
    # representation, just as the cross-language site contract fixtures do.
    try: models[case['model']].model_validate_json(json.dumps(case['value']));accepted=True
    except ValueError: accepted=False
    assert accepted==case['valid'],case['name']
sys.stdout.reconfigure(encoding='utf-8')
print(json.dumps(dict(cases=cases,legacy=legacy,full=full,baseline=archive),ensure_ascii=False))
