# Infrastructure Health Report

**Date** : 2026-08-08T12:39:48.521966+00:00

**Résultat** : 8/8 checks OK

| Check | Type | Cible | Statut | Détail |
|---|---|---|---|---|
| GitHub | http | https://github.com | ✅ | HTTP 200 — 0.139s |
| Docker Hub | http | https://hub.docker.com | ✅ | HTTP 200 — 0.146s |
| Terraform Registry | http | https://registry.terraform.io | ✅ | HTTP 200 — 0.106s |
| GitHub TLS | tls | github.com:443 | ✅ | Expire dans 53 jours |
| Docker Hub TLS | tls | hub.docker.com:443 | ✅ | Expire dans 57 jours |
| GitHub SSH | tcp | github.com:22 | ✅ | 0.019s |
| Google DNS | tcp | 8.8.8.8:53 | ✅ | 0.001s |
| GitHub DNS | dns | github.com | ✅ | Résolu: 140.82.116.3 |
