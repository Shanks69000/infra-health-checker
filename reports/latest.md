# Infrastructure Health Report

**Date** : 2026-07-29T19:10:19.157973+00:00

**Résultat** : 8/8 checks OK

| Check | Type | Cible | Statut | Détail |
|---|---|---|---|---|
| GitHub | http | https://github.com | ✅ | HTTP 200 — 0.339s |
| Docker Hub | http | https://hub.docker.com | ✅ | HTTP 200 — 0.22s |
| Terraform Registry | http | https://registry.terraform.io | ✅ | HTTP 200 — 0.121s |
| GitHub TLS | tls | github.com:443 | ✅ | Expire dans 63 jours |
| Docker Hub TLS | tls | hub.docker.com:443 | ✅ | Expire dans 67 jours |
| GitHub SSH | tcp | github.com:22 | ✅ | 0.056s |
| Google DNS | tcp | 8.8.8.8:53 | ✅ | 0.003s |
| GitHub DNS | dns | github.com | ✅ | Résolu: 140.82.114.3 |
