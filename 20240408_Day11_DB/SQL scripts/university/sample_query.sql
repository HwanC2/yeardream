# Query : instructor 10101이 2017년도 1학기에 근무했던 department를 출력해주세요.
select dept_name
from instructor join inst_dept on instructor.ID = inst_dept.i_id
				join department on inst_dept.d_id = department.ID
where semester = '2017-1'