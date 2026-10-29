# Import Dependencies
import os
from typing import Dict, List
from firecrawl import Firecrawl
from firecrawl.v2.types import SearchData
from dotenv import load_dotenv

load_dotenv()


class FirecrawlService:
    def __init__(self):
        api_key = os.getenv("FIRECRAWL_API_KEY")
        if not api_key:
            raise ValueError("Missing Firecrawl API key in environment variables.")
        self.app = Firecrawl(api_key=api_key)

    def _normalize_search_results(self, search_data: SearchData) -> List[Dict[str, any]]:
        """Flatten Firecrawl v2 SearchData into simple dict entries."""
        if not search_data:
            return []

        combined: List[Dict[str, any]] = []
        for bucket in (search_data.web or []):
            data = bucket.model_dump() if hasattr(bucket, "model_dump") else bucket
            data["url"] = data.get("url") or (data.get("metadata") or {}).get("url")
            data["description"] = data.get("description") or (data.get("metadata") or {}).get("description")
            combined.append(data)
        for bucket in (search_data.news or []):
            data = bucket.model_dump() if hasattr(bucket, "model_dump") else bucket
            data["url"] = data.get("url") or (data.get("metadata") or {}).get("url")
            data["description"] = data.get("description") or (data.get("metadata") or {}).get("description")
            combined.append(data)
        for bucket in (search_data.images or []):
            data = bucket.model_dump() if hasattr(bucket, "model_dump") else bucket
            data["url"] = data.get("url") or (data.get("metadata") or {}).get("url")
            combined.append(data)
        return combined

    # Search Functionality
    def search_companies(self, query: str, num_results: int = 5) -> List[Dict[str, any]]:
        try:
            raw_results = self.app.search(
                query=f"{query} company pricing",
                limit=num_results,
            )
            return self._normalize_search_results(raw_results)
        except Exception as e:
            print(e)
            return []
        
    # Scrape Functionality
    def scrape_company_pages(self, url: str):
        try:
            cleaned_url = url.strip()
            if not cleaned_url:
                return None
            return self.app.scrape(cleaned_url, formats=["markdown"])
        except Exception as e:
            print(e)
            return None
            
