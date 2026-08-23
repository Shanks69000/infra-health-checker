# Infrastructure Health Report

**Date** : 2026-08-23T18:23:14.944440+00:00

**Résultat** : 8/8 checks OK

| Check | Type | Cible | Statut | Détail |
|---|---|---|---|---|
| GitHub | http | https://github.com | ✅ | HTTP 200 — 0.154s |
| Docker Hub | http | https://hub.docker.com | ✅ | HTTP 200 — 0.168s |
| Terraform Registry | http | https://registry.terraform.io | ✅ | HTTP 200 — 0.061s |
| GitHub TLS | tls | github.com:443 | ✅ | Expire dans 38 jours |
| Docker Hub TLS | tls | hub.docker.com:443 | ✅ | Expire dans 79 jours |
| GitHub SSH | tcp | github.com:22 | ✅ | 0.017s |
| Google DNS | tcp | 8.8.8.8:53 | ✅ | 0.002s |
| GitHub DNS | dns | github.com | ✅ | Résolu: 140.82.114.3 |
