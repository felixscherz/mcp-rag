# mcp-rag

Connecting a RAG application to open-webui by means of MCP

## Bare bones MCP PoC

```bash
pip install mcp[cli]
```

- look up documentation on sse snippets
- run server using uvicorn
- doesnt work -> look up documentation in `SseServerTranpsort` class whcih differs from MCP website
- change Route -> Mount for starlette_app, then it works 
- starlette gives 307 temporary redirect, testing it with curl shows that it is due to a missing trailing
slash
- looked up on github repo, there the routes end with trailing slash for server code, especially the
`sse = SseServerTransport("/messages/")` part which I guess tells the client what to call
- add some prompts and check on client side

