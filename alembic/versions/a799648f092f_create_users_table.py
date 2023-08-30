"""create users table

Revision ID: a799648f092f
Revises: 
Create Date: 2023-08-29 17:19:57.175395

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'a799648f092f'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table("tblUsers",
                    sa.Column("Id", sa.Integer, primary_key=True, nullable=False),
                    sa.Column("Email", sa.String, nullable=False, unique=True),
                    sa.Column("Password", sa.String, nullable=False),
                    sa.Column("CreatedDate", sa.TIMESTAMP(timezone=True), server_default=sa.text('now()'), nullable=False)
                    )

def downgrade() -> None:
    op.drop_table("tblUsers")