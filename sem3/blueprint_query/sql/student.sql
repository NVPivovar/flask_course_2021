select s_name,birthday from student join s_group using(g_id) where g_index = '$group_index'