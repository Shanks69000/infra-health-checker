# Infrastructure Health Report

**Date** : 2026-08-28T08:55:09.750190+00:00

**Résultat** : 8/8 checks OK

| Check | Type | Cible | Statut | Détail |
|---|---|---|---|---|
| GitHub | http | https://github.com | ✅ | HTTP 200 — 0.318s |
| Docker Hub | http | https://hub.docker.com | ✅ | HTTP 200 — 0.244s |
| Terraform Registry | http | https://registry.terraform.io | ✅ | HTTP 200 — 0.114s |
| GitHub TLS | tls | github.com:443 | ✅ | Expire dans 33 jours |
| Docker Hub TLS | tls | hub.docker.com:443 | ✅ | Expire dans 75 jours |
| GitHub SSH | tcp | github.com:22 | ✅ | 0.05s |
| Google DNS | tcp | 8.8.8.8:53 | ✅ | 0.002s |
| GitHub DNS | dns | github.com | ✅ | Résolu: 140.82.114.4 |
