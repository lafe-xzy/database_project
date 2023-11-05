# 接口文档

web界面流程图：
![image](https://github.com/lafe-xzy/database_project/assets/134926682/37836731-42c6-456b-bd8d-7d46a20489ac)

> 应该有的功能

1. sign_up (user_name, password)      return user_id if success or 0 if fail;
2. log_in (user_id, password)        return 1 if success or 0 if fail;
3. log_out ()      return 1 if success of 0 if fail;
4. destroy (user_id)      return 1 if success or 0 if fail;
5. change_name (new_name)      return 1 if success or 0 if fail;
6. change_password (new_password)      return 1 if success or 0 if fail;

7. get_campus_id_by_name (campus_name)      return campus_id;
8. list_cafeteria_name (campus_id)          return list_of_cafeteria_name;
9. get_cafeteria_id_by_name (campus_id, cafeteria_name)      return cafeteria_id;
10. list_dish_name (campus_id, cafeteria_id)      return list_of_dish_name;
11. get_dish_id_by_name (campus_id, cafeteria_id, server_time_period, dish_name)      return dish_id;

12. get_comment_by_campus (campus_id)
13. get_comment_by_cafeteria (campus_id, cafeteria_id)
14. get_comment_by_time (campus_id, cafeteria_id, time_period)
15. get_comment_by_dish (campus_id, cafeteria_id, time_period, dish_id)
16. get_comment_by_userID (user_id)

17. comment (user_id, campus_id, cafeteria_id, server_time_period, dish_id, text)      return comment_id if success or 0 if fail;
18. del_comment (user_id, campus_id, cafeteria_id, server_time_period, dish_id)      return 1 if success or 0 if fail;
