from mtai.base import MTAIBase


class Bios(MTAIBase):
    """Bios Class used across defined."""

    @classmethod
    def list(cls):
        """
        List all bios.
        Returns:
            JSON Response
        """
        return cls().requests.get("/bios/list")