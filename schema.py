from pydantic import BaseModel,Field

class Learningpath(BaseModel):
    learning_stages:list[str]=Field(
        desciption=(
            "Ordered list of learning stages, from begineer to advaced."
            "must reflect a logical progression, not a random grouping."
            "For narrow skills, this list may be short(even 1-2 stages)."
        )
    )
    key_topics:list[str]=Field(
        description=(
            "Concrete topics/subskills the learner needs to cover, ordered"
            "so that earlier topics are prerequisites for later ones."
        )
    )
    learning_goal_summary:str=Field(
        description=(
            "A short paragraph explaning the overall progression logic -"
            "why the stages/topics are ordered this way."
        )
    )