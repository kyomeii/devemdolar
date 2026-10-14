---
title: On the job
description: CNPJ, taxes, getting paid, emergency fund, remote communication, and overemployment.
---

Congrats, you made it. Now the mission is different: **don't fuck it up**, get paid properly, pay less tax (legally), and prepare for the day everything goes to shit. Because it will. I got canned from two contracts two weeks apart, and the only thing that saved me was having money saved up.

## Bureaucracy: how to get paid

### Open a CNPJ

Almost every foreign contract is as a **contractor** (service provider), so you'll need a company, which in Brazil means opening a CNPJ (a business tax ID). A few things you need to know (and confirm with an accountant, because tax rules change all the time):

- **MEI won't work.** MEI (Brazil's micro-entrepreneur regime) doesn't allow software development, data analysis, or IT consulting on its list of permitted activities. Don't get cute and open a MEI with the wrong CNAE (business activity code).
- **Simples Nacional** (the simplified small-business tax regime) is the most common regime for people starting out. For IT activities, what defines your tax rate is the **Fator R** (the "R factor," payroll-to-revenue ratio): if your payroll (including your own pró-labore, the salary you pay yourself as a partner) is **at least 28% of revenue**, you fall into **Anexo III** (Annex III), which starts at 6%. If it's less, you fall into **Anexo V** (Annex V), which starts at 15.5%. That's why every accountant will tell you to take a 28% pró-labore.
- **Service exports are exempt:** since your client is outside Brazil and pays in foreign currency, export revenue doesn't pay ISS, PIS, and COFINS (municipal service tax and federal social contributions). In practice, your effective rate ends up way lower than the table's. Your accountant needs to know it's an export, otherwise you pay taxes for nothing.
- **Tax reform:** CBS and IBS (the new consumption taxes) are being phased in starting in 2026, but service exports remain immune. Still, keep an eye on it.
- **Dividends:** since 2026, if a single company pays you more than R$ 50k per month in dividends, there's a 10% income tax withheld at source on the **entire** amount (not just what goes over 50k), and there's also a minimum annual tax for people making more than R$ 600k per year. If you've reached that level, congrats, and talk to your accountant.

Look for an **accounting firm that specializes in people who export services**. There are plenty online that already do this on autopilot, and they charge a few hundred reais a month. Worth every penny.

Sounds like a lot, but relax: I barely worried about any of this myself. I did everything through **Contabilizei** (a Brazilian online accounting firm), and they handled the whole process. Here and there I had to do something, but nothing too complicated.

### How the money gets to you

There are two main ways:

1. **Hiring platform** (Deel, Remote, Oyster, and the like): the company hires you through them, you send your invoice through the platform, and withdraw to your account. Easy, but the platform sometimes eats a chunk on withdrawal.
2. **Direct invoice:** you send the invoice to the company every month and they transfer it to your international account.

To receive, the most common options are **Wise, Payoneer, Husky (now owned by Nomad), Inter (global account), Nomad, and Avenue**. What matters is the **spread** (the difference between the exchange rate they give you and the commercial rate) and the fixed fees. Seems like nothing, but a 1% difference on 5k dollars is 50 dollars **every month**, 600 a year. Compare.

I recommend **[Wise](https://wise.com)**. You get a USD account in your name, they convert at the commercial rate with a fee shown right in your face before you confirm, and the money lands in your company's account with no surprises.

> **Not Brazilian?** The spirit is the same: figure out your country's self-employed/simplified company regime (monotributo in Argentina, RESICO in Mexico, régimen simple in Colombia, boleta de honorarios in Chile) and find an accountant who already works with people working for foreign companies.

## Emergency fund

As a PJ (a contractor billing through your own company), you don't get FGTS (the mandatory severance fund), no unemployment insurance, no 40% severance penalty. Contractor contracts usually end with two weeks' notice, sometimes zero. Layoffs abroad happen by email, on a Friday, and you find out when your Slack access disappears.

So:

- **Build a fund of at least 6 months** of living expenses before you start spending like you're rich.
- **Don't inflate your lifestyle** in the first month. The new car can wait.
- **Set aside the tax money** as soon as you get paid, so you don't get caught off guard.
- **Think about retirement yourself.** Nobody's going to do it for you. INSS (Brazilian social security) on the minimum pró-labore won't support you in old age.

## Communication

Remote work lives and dies by communication. The guy who delivers little but communicates well lasts longer than the genius who disappears. Ideally, you deliver well **and** communicate well.

- **Communicate all the time.** Nobody can see you. If you don't say what you're doing, as far as your manager is concerned, you're doing nothing.
- **But skip the essay.** Americans don't want extra context. None of that "I finished the task, but there was an issue that led to another one, so I had to touch this other thing, blah blah blah." Just: **"I've completed this task."** If they want more, they'll ask. Context only goes in when it changes something for the reader (it's late, it needs a decision, it broke something else).
- **Take the credit.** Americans love it, and they expect you to do it too. It's **"I did this,"** not "the team did this." Brazilians have a habit of diluting their own work into "we," and then nobody knows it was you.
- **Don't just send "hi".** Send "Hi, so-and-so, I've got a problem with the X deploy, already tried Y and Z, can you help me?" all at once. Foreigners hate a "Hi" followed by waiting for a reply. There's even a website about it: [nohello.net](https://nohello.net).
- **Write updates.** At the end of the day (or week), send a summary of what you did, what you're going to do, and what's blocking you. Your manager will love it, and it becomes proof of your work when review time comes.
- **Ask in public channels, not in DMs.** That way more people can help, and the answer is on record for the next person.
- **"I don't know, but I'll find out"** is an excellent answer. Making up an answer isn't.
- **Didn't understand? Ask them to repeat.** "Sorry, could you repeat that?" or "Just to make sure I got it right, you mean...". Nobody will think you're dumb, they'll think you're careful. Pretending you understood and delivering the wrong thing, now that's dumb.
- **Document.** A decision made on a call that wasn't written down anywhere doesn't exist.

## Time zones

Brasília is UTC-3 and has no daylight saving time. The rest of the world does, so the difference changes twice a year:

| Region | Difference from Brasília |
|---|---|
| US East Coast (New York) | 1 to 2 hours behind |
| US West Coast (California) | 4 to 5 hours behind |
| UK / Portugal | 3 to 4 hours ahead |
| Central Europe (Germany, Netherlands, Spain) | 4 to 5 hours ahead |

Working for the East Coast is a breeze. For California, you'll have meetings at 6 p.m. For Europe, you'll have calls at 7 a.m. Agree from the start on your **overlap hours** with the team and be available during them, always.

## Holidays and vacation

- Brazilian holidays aren't holidays for foreigners. Carnival is a working day, and you need to give advance notice if you're not working.
- A lot of American companies stop for Thanksgiving, the 4th of July, and the end of the year. Enjoy it.
- Contractors usually **don't get paid vacation**. If it's not in the contract, negotiate, and always give plenty of notice.

## Deliver and be seen

- **Understand the business.** Remember the [Technical page](/en/technical/)? Whoever just executes tickets can be replaced by AI. Whoever understands why the ticket exists can't.
- **Be the guy who fixes things.** Take the annoying problem nobody wants. That's how you earn trust fast.
- **Do 1:1s with your manager** and ask straight up: "How am I doing? Is there anything I should be doing differently?"
- **Keep a brag document:** a list of everything you delivered, with numbers. It's useful for reviews, for asking for a raise, and, look at that, for updating your resume.

## AI at work

- **Read the company's policy** before throwing code or data into any AI. A lot of companies only allow the tools they pay for themselves.
- **Never paste client data, passwords, or API keys** into a personal AI account. It's the fastest way to get fired for cause.
- **You're responsible for everything the AI writes.** "Claude did it" is not an excuse. Review it.

## Overemployment (OE)

I've had two contracts at the same time, and I do again. I'm not going to pretend I don't. But if you're going to do it, do it right:

- **Read the contract.** Contractors can usually have other clients, but if there's an exclusivity clause, you're breaching the contract. Know the risk you're taking.
- **Never let quality slip.** The moment you start delivering badly, you lose both. OE only works if you're fucking good (again: master your stack).
- **Separate everything:** computer, accounts, email, browser. Never use one job's equipment for the other's work.
- **Manage your calendar** like your life depends on it. Block time on both calendars.
- **Keep your mouth shut.** Don't tell coworkers, don't post about it on LinkedIn.
- **Don't update your LinkedIn.** I don't update mine unless it's absolutely necessary (like when I'm unemployed). If they ask you to update it, pretend you didn't see it. If they insist, then there's no way around it, that's the risk you take.

## When it ends

Because it will end, sooner or later:

- **Don't burn bridges.** Leave on good terms, hand over properly, say thanks. The world is small, and a lot of people who worked with you will refer you in the future.
- **Ask for LinkedIn recommendations** while everyone still remembers you.
- **Never fully stop job hunting.** Even when employed, keep adding people on LinkedIn, take calls with recruiters, do an interview every now and then. That way, when the Friday email arrives, you already have somewhere to start.

And when you're on the other side, earning in a strong currency, come back here and **write your story**. That's how this site gets better.
