from model.group import Group


def test_modify_group_name(app):
	if app.group.count_group() == 0:
		app.group.create(Group(header="test_header"))
	old_groups = app.group.get_group_list()
	group = Group(name="New name")
	group.id = old_groups[0].id
	app.group.modify_first_group(Group(name="New name"))
	new_groups = app.group.get_group_list()
	assert len(old_groups) == len(new_groups)
	old_groups[0] = group
	assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


# def test_modify_group_header(app):
# 	if app.group.count_group() == 0:
# 		app.group.create(Group(footer="test_footer"))
# 	old_groups = app.group.get_group_list()
# 	app.group.modify_first_group(Group(header="New footer"))
# 	new_groups = app.group.get_group_list()
# 	assert len(old_groups) == len(new_groups)
