import { z } from 'zod/v4';
import { PictureSourceShape } from './generated/picture_source';

export const PictureSourceSchema = PictureSourceShape;
export type PictureSource = z.infer<typeof PictureSourceSchema>;
