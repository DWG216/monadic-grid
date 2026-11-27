# Sealed registrations

Some predictions are registered here by fingerprint before their code is written or run, and the text is published later.

Each line is the SHA-256 of a random salt followed by the exact bytes of the registration file. When a registration is opened, its file and salt are published next to its line, and anyone can check it:

```
python3 -c "import hashlib,sys; s=open(sys.argv[2]).read().strip(); print(hashlib.sha256(s.encode()+open(sys.argv[1],'rb').read()).hexdigest())" PREDICTIONS_tNNN.md PREDICTIONS_tNNN.md.salt
```

The commit that adds a line fixes its date; the line is never edited afterwards except to mark it opened.

| Sealed (UTC) | Fingerprint | Status |
|---|---|---|
