# Standard Crypto Engineering Take-Home Challenge

The task is to answer several questions about rates of voter turnout for the community-run governance process of the [Aave](https://aave.com/) protocol. It isn’t expected that you’ll be immediately familiar with all components involved in this question. This exercise is meant to assess both technical ability and ability to develop an introductory level of understanding of new concepts.

The questions we want to answer are as follows:

1. Which are the top 20 addresses with the highest rates of participation for Aave governance proposals on Snapshot.org, and what are each of their participation rates?
   - Find all proposal ids
   - Find all voters for all proposals
   - See which votes appear the most often
2. What rate of Snapshot participation for Aave does the University of Pennsylvania blockchain student organization have? (UPenn’s address used for voting is `0x070341aA5Ed571f0FB2c4a5641409B1A46b4961b`)
   - Same as above, but only filter for the upenn address

For anything with which you are not familiar, the following high-level glossary is provided:

**Snapshot.org:** A webapp for communities to submit and vote on proposals. Primarily used as a lightweight system of governance for crypto projects that choose to be community-run. Hosts a free and public API for issuing queries against its vote and proposal data.

**Address:** An identifier for each of the actors within a blockchain ecosystem. Typically a long and hexadecimal-formatted string, such as `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2`.

**Aave**: A notable project within the Ethereum blockchain ecosystem, used by people seeking to lend or to borrow crypto assets. Aave is one of many projects that has elected for a decentralized system of governance, meaning its evolution is partially governed by its Snapshot space, hosted here: [https://snapshot.org/#/aave.eth](https://snapshot.org/#/aave.eth)

# Submission

Please provide either an archive folder or a link to a repository with at least the following:

- A README with the answers to the questions posed by this challenge
- Your code used in deriving answers to these questions
- Instructions in README for rerunning your scripts and arriving to your answers

# Notes and Tips

- If searching for a starting point, try clicking through a few Snapshot proposals in the browser and try to find the same data via queries to the Snapshot API.
- You may use any languages, libraries, and editors you choose.
- You should not need to use the `snapshot.js` library nor the webhooks functionality provided by Snapshot.
- Be mindful of the default pagination used by Snapshot’s API, so as to not miss any data.
- Be sure to filter on the correct Snapshot ‘space’ for Aave when fetching proposals.
- Snapshot has recently added a limit to the number of votes it will allow a client to retrieve for a given proposal. You should expect you will encounter an error from the API. We’ve brought this to the Snapshot team’s attention and requested a workaround, but in the interim we acknowledge that for now an implementation must rely on partial data.
- Aim for proof-of-concept quality of code. You need not optimize for production readiness. A quick pass for legibility, a few organizational comments for the reader, and a removal of scratch work and unused code is plenty.
- Although Snapshot provides a system for weighted voting, for these questions the voting power of each voter is irrelevant — we care only about each voter’s rate of turnout.
- If anything is confusing or unclear, please don’t hesitate to reach out. Parts of this problem are deliberately under-specified, but never meant to leave you stuck.