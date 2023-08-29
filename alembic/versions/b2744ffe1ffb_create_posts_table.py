"""create posts table

Revision ID: b2744ffe1ffb
Revises: a799648f092f
Create Date: 2023-08-29 17:25:52.924563

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'b2744ffe1ffb'
down_revision: Union[str, None] = 'a799648f092f'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table("tblPosts",
                    sa.Column("Id", sa.Integer, primary_key=True, nullable=False),
                    sa.Column("Title", sa.String, nullable=False),
                    sa.Column("Content", sa.String, nullable=False),
                    sa.Column("Published", sa.Boolean, server_default='True', nullable=False),
                    sa.Column("CreatedDate", sa.TIMESTAMP(timezone=True), server_default=sa.text('now()'), nullable=False),
                    )


def downgrade() -> None:
    op.drop_table("tblPosts")
