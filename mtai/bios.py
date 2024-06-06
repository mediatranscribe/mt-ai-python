"""Entry point defined here."""

from mtai.base import MTAIBase


class Bio(MTAIBase):
    """A class to handle operations related to bios."""

    @classmethod
    def list(cls):
        """
        List all bios.

        Returns:
            JSON: A JSON response containing the list of bios.
        """
        return cls().requests.get("/bios/list")

    @classmethod
    def create_mentor_mentee_bio(
        cls, country, job_title, interests, is_mentor=False, max_length=300
    ):
        """
        Create a new bio with the country, job_title, interests, is_mentor, max_length.

        Args:
            country (str): The user's country
            job_title (str): The user's job title
            interests (str): the user's interests
            is mentor (str): Whether the user is a mentor
            max length (str): The maximum length

        Returns:
            JSON: A JSON response containing the created bio.
        """
        bio_data = {
            "country": country,
            "job_title": job_title,
            "interests": interests,
            "is_mentor": is_mentor,
            "max_length": max_length,
        }
        return cls().requests.post("/bios/mentor-mentee-bio-create", json=bio_data)

    def bio_text_create(cls, text, output_format, max_length=300):
        """
        Create a new bio with the text, output_format, max_length.

        Args:
            text (str): The text to be used
            output_format (str): The way the results should be presented
            max_length (str): The maximum length

        Returns:
            JSON: A JSON response containing the created bio.
        """
        bio_data = {
            "text": text,
            "output_format": output_format,
            "max_length": max_length,
        }
        return cls().requests.post("/bios/bio_text_create", json=bio_data)

    @classmethod
    def bio_retrieve(
        cls,
        id,
    ):
        """
        Retrieve a bio by its ID.

        Args:
            bio_id (str): The ID of the bio to retrieve.

        Returns:
            JSON: A JSON response containing the bio details.
        """
        return cls().requests.get(f"/bios/retrieve/{id}")

    @classmethod
    def bio_delete(cls, id):
        """
        Delete a bio by its ID.

        Args:
            bio_id (str): The ID of the bio to delete.

        Returns:
            JSON: A JSON response confirming the deletion.
        """
        return cls().requests.delete(f"/bios/delete/{id}")
