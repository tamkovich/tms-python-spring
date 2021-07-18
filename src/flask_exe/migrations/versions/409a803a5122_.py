"""empty message

Revision ID: 409a803a5122
Revises: 
Create Date: 2021-07-14 21:56:09.848046

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "409a803a5122"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("users")
    op.drop_table("car")
    op.drop_table("brand")
    op.add_column("product", sa.Column("amount", sa.Integer(), nullable=True))
    op.add_column("product", sa.Column("comment", sa.String(), nullable=True))
    op.drop_column("product", "count")
    op.drop_column("product", "coment")
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        "product", sa.Column("coment", sa.TEXT(), autoincrement=False, nullable=True)
    )
    op.add_column(
        "product", sa.Column("count", sa.INTEGER(), autoincrement=False, nullable=True)
    )
    op.drop_column("product", "comment")
    op.drop_column("product", "amount")
    op.create_table(
        "brand",
        sa.Column(
            "id",
            sa.INTEGER(),
            server_default=sa.text("nextval('brand_id_seq'::regclass)"),
            autoincrement=True,
            nullable=False,
        ),
        sa.Column("name", sa.VARCHAR(length=50), autoincrement=False, nullable=True),
        sa.PrimaryKeyConstraint("id", name="brand_pkey"),
        postgresql_ignore_search_path=False,
    )
    op.create_table(
        "car",
        sa.Column("id", sa.INTEGER(), autoincrement=True, nullable=False),
        sa.Column("model", sa.VARCHAR(length=50), autoincrement=False, nullable=True),
        sa.Column("release_year", sa.INTEGER(), autoincrement=False, nullable=True),
        sa.Column("brand_id", sa.INTEGER(), autoincrement=False, nullable=True),
        sa.ForeignKeyConstraint(["brand_id"], ["brand.id"], name="car_brand_id_fkey"),
        sa.PrimaryKeyConstraint("id", name="car_pkey"),
    )
    op.create_table(
        "users",
        sa.Column("id", sa.INTEGER(), autoincrement=True, nullable=False),
        sa.Column(
            "first_name", sa.VARCHAR(length=50), autoincrement=False, nullable=True
        ),
        sa.Column("coment", sa.TEXT(), autoincrement=False, nullable=True),
        sa.PrimaryKeyConstraint("id", name="users_pkey"),
    )
    # ### end Alembic commands ###
