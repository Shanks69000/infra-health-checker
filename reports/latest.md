# Infrastructure Health Report

**Date** : 2026-11-10T22:47:43.089975+00:00

**Résultat** : 8/8 checks OK

| Check | Type | Cible | Statut | Détail |
|---|---|---|---|---|
| GitHub | http | https://github.com | ✅ | HTTP 200 — 0.267s |
| Docker Hub | http | https://hub.docker.com | ✅ | HTTP 200 — 0.255s |
| Terraform Registry | http | https://registry.terraform.io | ✅ | HTTP 200 — 0.16s |
| GitHub TLS | tls | github.com:443 | ✅ | Expire dans 78 jours |
| Docker Hub TLS | tls | hub.docker.com:443 | ✅ | Expire dans 80 jours |
| GitHub SSH | tcp | github.com:22 | ✅ | 0.044s |
| Google DNS | tcp | 8.8.8.8:53 | ✅ | 0.014s |
| GitHub DNS | dns | github.com | ✅ | Résolu: 140.82.114.3 |
