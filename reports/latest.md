# Infrastructure Health Report

**Date** : 2026-10-28T22:08:16.824466+00:00

**Résultat** : 8/8 checks OK

| Check | Type | Cible | Statut | Détail |
|---|---|---|---|---|
| GitHub | http | https://github.com | ✅ | HTTP 200 — 0.271s |
| Docker Hub | http | https://hub.docker.com | ✅ | HTTP 200 — 0.248s |
| Terraform Registry | http | https://registry.terraform.io | ✅ | HTTP 200 — 0.128s |
| GitHub TLS | tls | github.com:443 | ✅ | Expire dans 32 jours |
| Docker Hub TLS | tls | hub.docker.com:443 | ✅ | Expire dans 72 jours |
| GitHub SSH | tcp | github.com:22 | ✅ | 0.043s |
| Google DNS | tcp | 8.8.8.8:53 | ✅ | 0.011s |
| GitHub DNS | dns | github.com | ✅ | Résolu: 140.82.114.3 |
