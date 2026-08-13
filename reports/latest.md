# Infrastructure Health Report

**Date** : 2026-08-13T13:01:40.537705+00:00

**Résultat** : 8/8 checks OK

| Check | Type | Cible | Statut | Détail |
|---|---|---|---|---|
| GitHub | http | https://github.com | ✅ | HTTP 200 — 0.204s |
| Docker Hub | http | https://hub.docker.com | ✅ | HTTP 200 — 1.268s |
| Terraform Registry | http | https://registry.terraform.io | ✅ | HTTP 200 — 0.13s |
| GitHub TLS | tls | github.com:443 | ✅ | Expire dans 48 jours |
| Docker Hub TLS | tls | hub.docker.com:443 | ✅ | Expire dans 52 jours |
| GitHub SSH | tcp | github.com:22 | ✅ | 0.024s |
| Google DNS | tcp | 8.8.8.8:53 | ✅ | 0.015s |
| GitHub DNS | dns | github.com | ✅ | Résolu: 140.82.113.3 |
