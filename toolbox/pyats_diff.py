from genie.utils.diff import Diff
import toolbox.database as db
import json

def compare_output_before_after(hostname, test_name):

    result_before = json.loads(db.get_output_test(hostname, test_name, "before"))
    result_after = json.loads(db.get_output_test(hostname, test_name, "after"))

    dd = Diff(result_before, result_after, mode = 'modified')

    dd.findDiff()
    print(dd)