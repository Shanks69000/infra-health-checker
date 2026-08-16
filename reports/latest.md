# Infrastructure Health Report

**Date** : 2026-08-16T18:22:25.713913+00:00

**Résultat** : 8/8 checks OK

| Check | Type | Cible | Statut | Détail |
|---|---|---|---|---|
| GitHub | http | https://github.com | ✅ | HTTP 200 — 0.118s |
| Docker Hub | http | https://hub.docker.com | ✅ | HTTP 200 — 0.151s |
| Terraform Registry | http | https://registry.terraform.io | ✅ | HTTP 200 — 0.109s |
| GitHub TLS | tls | github.com:443 | ✅ | Expire dans 45 jours |
| Docker Hub TLS | tls | hub.docker.com:443 | ✅ | Expire dans 86 jours |
| GitHub SSH | tcp | github.com:22 | ✅ | 0.017s |
| Google DNS | tcp | 8.8.8.8:53 | ✅ | 0.002s |
| GitHub DNS | dns | github.com | ✅ | Résolu: 140.82.113.4 |
