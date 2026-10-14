// ---------------------------------------------------------------
// Configurações do site. É só trocar os valores aqui.
// Site settings. Just change the values here.
// ---------------------------------------------------------------

// Endereço final do site (sem barra no fim).
export const SITE_URL = 'https://devemdolar.workers.dev';

// Endereço do repositório no GitHub.
export const REPO_URL = 'https://github.com/kyomeii/devemdolar';

// E-mail de contato pra propostas de propaganda/parceria. Deixe '' pra esconder.
// Use um e-mail criado só pra isso, não o seu pessoal.
export const CONTACT_EMAIL = '';

// Carteiras pra doação em cripto. Deixe '' nas que você não usar.
// Elas só aparecem no site quando estiverem preenchidas.
export const WALLETS = [
	{ coin: 'Bitcoin', network: 'Bitcoin (BTC)', address: '' },
	{ coin: 'USDT / USDC', network: 'Polygon / Ethereum / Base (EVM)', address: '' },
	{ coin: 'Solana / USDC', network: 'Solana (SOL)', address: '' },
];
