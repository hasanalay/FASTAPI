"""add foreign-key to posts table

Revision ID: 16a9a06d8350
Revises: b2744ffe1ffb
Create Date: 2023-08-29 17:30:16.616241

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '16a9a06d8350'
down_revision: Union[str, None] = 'b2744ffe1ffb'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column("tblPosts",sa.Column("owner_id", sa.Integer, nullable=False))
    op.create_foreign_key("fk_posts_owner_id", source_table="tblPosts", referent_table="tblUsers", local_cols=["owner_id"], remote_cols=["Id"], ondelete="CASCADE")


def downgrade() -> None:
    op.delete_constraint("fk_posts_owner_id", "tblPosts", type_="foreignkey")
    op.drop_column("tblPosts", "owner_id")
