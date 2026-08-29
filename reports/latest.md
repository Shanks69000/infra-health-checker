# Infrastructure Health Report

**Date** : 2026-08-29T05:30:15.995991+00:00

**Résultat** : 8/8 checks OK

| Check | Type | Cible | Statut | Détail |
|---|---|---|---|---|
| GitHub | http | https://github.com | ✅ | HTTP 200 — 0.124s |
| Docker Hub | http | https://hub.docker.com | ✅ | HTTP 200 — 0.232s |
| Terraform Registry | http | https://registry.terraform.io | ✅ | HTTP 200 — 0.104s |
| GitHub TLS | tls | github.com:443 | ✅ | Expire dans 32 jours |
| Docker Hub TLS | tls | hub.docker.com:443 | ✅ | Expire dans 74 jours |
| GitHub SSH | tcp | github.com:22 | ✅ | 0.017s |
| Google DNS | tcp | 8.8.8.8:53 | ✅ | 0.004s |
| GitHub DNS | dns | github.com | ✅ | Résolu: 140.82.112.4 |
