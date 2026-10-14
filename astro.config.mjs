// @ts-check
import { defineConfig } from 'astro/config';
import starlight from '@astrojs/starlight';
import { SITE_URL, REPO_URL } from './src/config.mjs';

export default defineConfig({
	site: SITE_URL,
	integrations: [
		starlight({
			title: 'Gringa',
			description:
				'Guia gratuito, open source e sem papo de coach pra trabalhar remoto pra fora ganhando em dólar ou euro.',
			logo: { src: './src/assets/logo.svg', replacesTitle: false },
			favicon: '/favicon.svg',
			defaultLocale: 'pt',
			locales: {
				pt: { label: 'Português', lang: 'pt-BR' },
				es: { label: 'Español', lang: 'es' },
				en: { label: 'English', lang: 'en' },
			},
			social: [{ icon: 'github', label: 'GitHub', href: REPO_URL }],
			editLink: { baseUrl: `${REPO_URL}/edit/main/` },
			lastUpdated: true,
			customCss: [
				'@fontsource-variable/inter',
				'@fontsource-variable/space-grotesk',
				'@fontsource/jetbrains-mono/400.css',
				'./src/styles/theme.css',
			],
			head: [
				{ tag: 'meta', attrs: { property: 'og:image', content: `${SITE_URL}/og.jpg` } },
				{ tag: 'meta', attrs: { name: 'twitter:card', content: 'summary_large_image' } },
				{ tag: 'meta', attrs: { name: 'twitter:image', content: `${SITE_URL}/og.jpg` } },
			],
			components: {
				Footer: './src/components/Footer.astro',
			},
			sidebar: [
				{
					label: 'O guia',
					translations: { es: 'La guía', en: 'The guide' },
					items: [
						'manifesto',
						'english',
						'technical',
						'resume',
						'linkedin',
						'job-hunting',
						'interview',
						'on-the-job',
					],
				},
				{
					label: 'Comunidade',
					translations: { es: 'Comunidad', en: 'Community' },
					items: ['companies', 'stories', 'contribute', 'support'],
				},
			],
		}),
	],
});
