import type { APIRoute } from 'astro';
import { rss } from '../../rss';

export const GET: APIRoute = ({ site }) => rss(site!);
