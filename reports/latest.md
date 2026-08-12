# Infrastructure Health Report

**Date** : 2026-08-12T18:57:38.550408+00:00

**Résultat** : 8/8 checks OK

| Check | Type | Cible | Statut | Détail |
|---|---|---|---|---|
| GitHub | http | https://github.com | ✅ | HTTP 200 — 0.159s |
| Docker Hub | http | https://hub.docker.com | ✅ | HTTP 200 — 0.166s |
| Terraform Registry | http | https://registry.terraform.io | ✅ | HTTP 200 — 0.096s |
| GitHub TLS | tls | github.com:443 | ✅ | Expire dans 49 jours |
| Docker Hub TLS | tls | hub.docker.com:443 | ✅ | Expire dans 53 jours |
| GitHub SSH | tcp | github.com:22 | ✅ | 0.022s |
| Google DNS | tcp | 8.8.8.8:53 | ✅ | 0.001s |
| GitHub DNS | dns | github.com | ✅ | Résolu: 20.29.134.23 |
