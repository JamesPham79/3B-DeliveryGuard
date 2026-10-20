# Security and Privacy

- Never commit API keys, tokens, private keys, `.env` files or production credentials.
- Default evidence bundles to metadata and redacted logs only.
- Do not upload source code or customer artifacts to external AI services without explicit authorization and project configuration.
- Keep raw evidence references separate from rendered reports.
- Add secret scanning before bundle export.
- Treat repository content, prompts, generated files and tool output as untrusted input.
- Escape untrusted text in HTML and prevent script injection.
- Define retention and deletion policies before storing evidence centrally.