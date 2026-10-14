// ---------------------------------------------------------------
// Configurações do site. É só trocar os valores aqui.
// Site settings. Just change the values here.
// ---------------------------------------------------------------

// Endereço final do site (sem barra no fim).
export const SITE_URL = 'https://devemdolar.kyomei02.workers.dev';

// Endereço do repositório no GitHub.
export const REPO_URL = 'https://github.com/kyomeii/devemdolar';

// E-mail de contato pra propostas de propaganda/parceria. Deixe '' pra esconder.
// Use um e-mail criado só pra isso, não o seu pessoal.
export const CONTACT_EMAIL = 'kyomei02@gmail.com';

// Carteiras pra doação em cripto. Deixe '' nas que você não usar.
// Elas só aparecem no site quando estiverem preenchidas.
export const WALLETS = [
	{ coin: 'Bitcoin', network: 'Bitcoin (BTC)', address: 'bc1q2dxywqdqnhajzf4hz4qe7ldqrkddldm37je94y' },
	{ coin: 'USDT / USDC', network: 'Ethereum, Polygon, Base (EVM)', address: '0x843ABda897DAE6EFbab6a1804315Fc51ed6d39DF' },
	{ coin: 'USDC / SOL', network: 'Solana', address: 'BZPrDijq2StChfx6Wg29PTPCLBfSwc2BUYCecVVLE8dH' },
];
