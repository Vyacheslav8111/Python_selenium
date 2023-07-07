from model.group import Group


def test_modify_group_name(app):
	if app.group.count_group() == 0:
		app.group.create(Group(header="test_header"))
	app.group.modify_first_group(Group(name="New name"))


def test_modify_group_header(app):
	if app.group.count_group() == 0:
		app.group.create(Group(footer="test_footer"))
	app.group.modify_first_group(Group(header="New footer"))
