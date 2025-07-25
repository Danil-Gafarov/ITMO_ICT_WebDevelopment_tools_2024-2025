from enum import Enum
from typing import Optional, List

from sqlmodel import SQLModel, Field, Relationship


class RaceType(str, Enum):
    director = "director"
    worker = "worker"
    junior = "junior"


class SkillWarriorLink(SQLModel, table=True):
    skill_id: Optional[int] = Field(
    default=None, foreign_key="skill.id", primary_key=True
    )
    warrior_id: Optional[int] = Field(
    default=None, foreign_key="warrior.id", primary_key=True
    )
    level: int | None


class Skill(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    name: str
    description: Optional[str] = ""
    warriors: List["Warrior"] = Relationship(back_populates="skills", link_model=SkillWarriorLink)


class ProfessionDefault(SQLModel):
    title: str
    description: str


class Profession(ProfessionDefault, table=True):
    id: int = Field(default=None, primary_key=True)
    title: str
    description: str
    warriors_prof: List["Warrior"] = Relationship(back_populates="profession")


class WarriorDefault(SQLModel):
    race: RaceType
    name: str
    level: int
    profession_id: Optional[int] = Field(default=None, foreign_key="profession.id")


class Warrior(WarriorDefault, table=True):
    id: int = Field(default=None, primary_key=True)
    profession_id: Optional[int] = Field(default=None, foreign_key="profession.id")
    profession: Optional[Profession] = Relationship(back_populates="warriors_prof")
    skills: Optional[List[Skill]] = Relationship(back_populates="warriors", link_model=SkillWarriorLink)


class WarriorProfessions(WarriorDefault):
    profession: Optional[Profession] = None


class WarriorWithFullDetails(WarriorDefault):
    profession: Optional[Profession] = None
    skills: List[Skill] = []