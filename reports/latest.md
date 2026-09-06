# Infrastructure Health Report

**Date** : 2026-09-06T14:52:57.402059+00:00

**Résultat** : 8/8 checks OK

| Check | Type | Cible | Statut | Détail |
|---|---|---|---|---|
| GitHub | http | https://github.com | ✅ | HTTP 200 — 0.175s |
| Docker Hub | http | https://hub.docker.com | ✅ | HTTP 200 — 0.182s |
| Terraform Registry | http | https://registry.terraform.io | ✅ | HTTP 200 — 0.136s |
| GitHub TLS | tls | github.com:443 | ✅ | Expire dans 84 jours |
| Docker Hub TLS | tls | hub.docker.com:443 | ✅ | Expire dans 87 jours |
| GitHub SSH | tcp | github.com:22 | ✅ | 0.029s |
| Google DNS | tcp | 8.8.8.8:53 | ✅ | 0.014s |
| GitHub DNS | dns | github.com | ✅ | Résolu: 140.82.114.3 |
