# Infrastructure Health Report

**Date** : 2026-08-03T14:31:45.151295+00:00

**Résultat** : 8/8 checks OK

| Check | Type | Cible | Statut | Détail |
|---|---|---|---|---|
| GitHub | http | https://github.com | ✅ | HTTP 200 — 0.159s |
| Docker Hub | http | https://hub.docker.com | ✅ | HTTP 200 — 0.108s |
| Terraform Registry | http | https://registry.terraform.io | ✅ | HTTP 200 — 0.102s |
| GitHub TLS | tls | github.com:443 | ✅ | Expire dans 58 jours |
| Docker Hub TLS | tls | hub.docker.com:443 | ✅ | Expire dans 62 jours |
| GitHub SSH | tcp | github.com:22 | ✅ | 0.017s |
| Google DNS | tcp | 8.8.8.8:53 | ✅ | 0.005s |
| GitHub DNS | dns | github.com | ✅ | Résolu: 140.82.114.3 |
