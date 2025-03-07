"""update user

Revision ID: 4e2b7338308f
Revises: 3275f116bf8c
Create Date: 2025-02-25 16:18:10.367007

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '4e2b7338308f'
down_revision: Union[str, None] = '3275f116bf8c'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('сonfirmed', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'сonfirmed')
    # ### end Alembic commands ###
