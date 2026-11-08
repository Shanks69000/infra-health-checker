# Infrastructure Health Report

**Date** : 2026-11-08T04:17:10.008922+00:00

**Résultat** : 8/8 checks OK

| Check | Type | Cible | Statut | Détail |
|---|---|---|---|---|
| GitHub | http | https://github.com | ✅ | HTTP 200 — 0.127s |
| Docker Hub | http | https://hub.docker.com | ✅ | HTTP 200 — 0.231s |
| Terraform Registry | http | https://registry.terraform.io | ✅ | HTTP 200 — 0.106s |
| GitHub TLS | tls | github.com:443 | ✅ | Expire dans 80 jours |
| Docker Hub TLS | tls | hub.docker.com:443 | ✅ | Expire dans 83 jours |
| GitHub SSH | tcp | github.com:22 | ✅ | 0.018s |
| Google DNS | tcp | 8.8.8.8:53 | ✅ | 0.001s |
| GitHub DNS | dns | github.com | ✅ | Résolu: 172.182.252.133 |
