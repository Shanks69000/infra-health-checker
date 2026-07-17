# Infrastructure Health Report

**Date** : 2026-07-17T13:20:52.406784+00:00

**Résultat** : 8/8 checks OK

| Check | Type | Cible | Statut | Détail |
|---|---|---|---|---|
| GitHub | http | https://github.com | ✅ | HTTP 200 — 0.166s |
| Docker Hub | http | https://hub.docker.com | ✅ | HTTP 200 — 0.282s |
| Terraform Registry | http | https://registry.terraform.io | ✅ | HTTP 200 — 0.095s |
| GitHub TLS | tls | github.com:443 | ✅ | Expire dans 75 jours |
| Docker Hub TLS | tls | hub.docker.com:443 | ✅ | Expire dans 79 jours |
| GitHub SSH | tcp | github.com:22 | ✅ | 0.033s |
| Google DNS | tcp | 8.8.8.8:53 | ✅ | 0.014s |
| GitHub DNS | dns | github.com | ✅ | Résolu: 140.82.114.3 |
