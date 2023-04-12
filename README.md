# Standard Crypto Engineering Take-Home Challenge

The task is to answer several questions about rates of voter turnout for the community-run governance process of the [Aave](https://aave.com/) protocol. It isn’t expected that you’ll be immediately familiar with all components involved in this question. This exercise is meant to assess both technical ability and ability to develop an introductory level of understanding of new concepts.

The questions we want to answer are as follows:

1. Which are the top 20 addresses with the highest rates of participation for Aave governance proposals on Snapshot.org, and what are each of their participation rates?
   - Find all proposal ids
   - Find all voters for all proposals
   - See which votes appear the most often
[('0x06c4865ab16c9C760622f19a313a2E637E2e66a2', 0.7347670250896058), ('0x0fF9B6AB6Ec58ceB6D5ae8a1690dd5a0959aD002', 0.7060931899641577), ('0x7A3BdeE62dd34faC317Ae61cd8B3bA7c27ada145', 0.7060931899641577), ('0x76AC6Ad4e4E7c2e0b4Ceeb30745bd53df3a85774', 0.7060931899641577), ('0x9Ba6baA919BAc9Acd901dF3Bfde848FE006D3caE', 0.7060931899641577), ('0x00432772Ed25d4Eb3C6EB26Dc461239b35cf8760', 0.7025089605734767), ('0x35E6fc00e3F190A8dFe15faa219368a01028ec14', 0.7025089605734767), ('0x0516cf37B67235E07aF38ad8E388d0E68089b0F2', 0.7025089605734767), ('0x1b5b4fCEDF1252cd92496a2fd5C593b39aC49b01', 0.7025089605734767), ('0x2D5823E8e8B4dfbf599a97566ff2A121Cc141d60', 0.7025089605734767), ('0x972a8B7D891B88220780421fE4D11f174354cEEd', 0.7025089605734767), ('0xbDa0136ea391e24a938793972726f8763150c7C3', 0.6989247311827957), ('0x344b1E4Ac175f16D3bA40A688cA928E3768E275a', 0.6989247311827957), ('0x707D306714FF28560f32bF9DAE973BD33cd851c5', 0.6989247311827957), ('0xD03Ad690ed8065EDfdC1E08197a3ebC71535A7ff', 0.6989247311827957), ('0x70Ddb5AbF21202602b57F4860eE1262a594a0086', 0.6989247311827957), ('0xc97370F22eD5ac4c7B24A8E1ca9D81FEbb3b9457', 0.6989247311827957), ('0x1B9DA462D07512Fa37021973d853B59dEbB761Dd', 0.6559139784946236), ('0x79ccEDbEFbfE6c95570d85e65f8B0aC0D6bd017B', 0.6487455197132617), ('0x183bDB344A07Ee3D27f07AC4799A56E4A2fE5439', 0.6451612903225806)]

2. What rate of Snapshot participation for Aave does the University of Pennsylvania blockchain student organization have? (UPenn’s address used for voting is `0x070341aA5Ed571f0FB2c4a5641409B1A46b4961b`)
   - Same as above, but only filter for the upenn address
0.5519713261648745

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