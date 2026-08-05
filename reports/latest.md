# Infrastructure Health Report

**Date** : 2026-08-05T08:30:17.542102+00:00

**Résultat** : 8/8 checks OK

| Check | Type | Cible | Statut | Détail |
|---|---|---|---|---|
| GitHub | http | https://github.com | ✅ | HTTP 200 — 0.057s |
| Docker Hub | http | https://hub.docker.com | ✅ | HTTP 200 — 0.218s |
| Terraform Registry | http | https://registry.terraform.io | ✅ | HTTP 200 — 0.207s |
| GitHub TLS | tls | github.com:443 | ✅ | Expire dans 56 jours |
| Docker Hub TLS | tls | hub.docker.com:443 | ✅ | Expire dans 60 jours |
| GitHub SSH | tcp | github.com:22 | ✅ | 0.005s |
| Google DNS | tcp | 8.8.8.8:53 | ✅ | 0.004s |
| GitHub DNS | dns | github.com | ✅ | Résolu: 140.82.116.3 |
