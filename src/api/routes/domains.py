"""Domain listing, groups, regions, categories, and tags."""

from typing import Optional

from fastapi import APIRouter, Depends, HTTPException, Query

from ..deps import get_config
from ...core.config import ConfigLoader, ConfigurationError

router = APIRouter(prefix="/api", tags=["domains"])


@router.get("/domains")
def list_domains(
    group: Optional[str] = Query(None, description="Filter by group/region"),
    category: Optional[str] = Query(None),
    tag: Optional[str] = Query(None),
    config: ConfigLoader = Depends(get_config),
):
    """List domains, optionally filtered by group, category, or tag."""
    try:
        if group:
            domains = config.get_enabled_domains(group)
        else:
            domains = config.list_domains()
    except ConfigurationError as e:
        raise HTTPException(status_code=400, detail=str(e))

    if category:
        domains = [d for d in domains if d.get("category") == category]
    if tag:
        domains = [d for d in domains if tag in d.get("tags", [])]

    return {"domains": domains, "count": len(domains)}


@router.get("/domains/{domain_id}")
def get_domain(domain_id: str, config: ConfigLoader = Depends(get_config)):
    """Get full config for a single domain."""
    all_domains = {d["id"]: d for d in config.domains_config.get("domains", [])}
    if domain_id not in all_domains:
        raise HTTPException(status_code=404, detail=f"Domain '{domain_id}' not found")
    return all_domains[domain_id]


@router.get("/groups")
def list_groups(config: ConfigLoader = Depends(get_config)):
    """List available domain groups."""
    return config.list_groups()


@router.get("/regions")
def list_regions(config: ConfigLoader = Depends(get_config)):
    """List available regions."""
    return config.list_regions()


@router.get("/categories")
def list_categories(config: ConfigLoader = Depends(get_config)):
    """List valid domain categories."""
    return config.list_categories()


@router.get("/tags")
def list_tags(config: ConfigLoader = Depends(get_config)):
    """List valid domain tags."""
    return config.list_tags()
