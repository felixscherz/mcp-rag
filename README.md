# mcp-rag

Connecting a RAG application to open-webui by means of MCP

## 1. Bare bones MCP PoC / Hello World

```bash
pip install mcp[cli]
```

- look up documentation on sse snippets
- run server using uvicorn
- doesnt work -> look up documentation in `SseServerTranpsort` class which differs from MCP website
- change Route -> Mount for starlette_app, then it works 
- starlette gives 307 temporary redirect, testing it with curl shows that it is due to a missing trailing
slash
- looked up on github repo, there the routes end with trailing slash for server code, especially the
`sse = SseServerTransport("/messages/")` part which I guess tells the client what to call
- add some prompts and check on client side

### Writeup

- I want to try out the model context protocol because I have been experimenting with RAG prototypes for use with
open-webui. MCP looks similar to LSP. Since server and client won't be on the same machine, we have to use the SSE
transport.
- MCP comes with some snippets on the official documentation, I had to adapt them a bit following the docstrings
provided by the mcp python library. Took me a while to get things working, initially dealt with 307 Temporary Redirect
errors since the server was sending the wrong endpoint.
- Test it! Build a small REPL that can interact with the server

### Goal

1. understand what MCP is
2. implement a simple server and client
3. try out function calling / tool usage


## 2. Implement a basic KnowlegdeBase

- I want to build a simple KnowledgeBase that we can stick into the MCP server and call through the client to retrieve
some context.


## 3. MCP Client + Open-WebUI
