import acme_corp.do_task as do_task

def test_perform_action():
    args = 'foo'
    input_data = 'bar'

    exp = f"Some results based on args:\n{args}\n and input_data:\n{input_data}\n"

    obs = do_task.perform_action(args, input_data)

    assert exp == obs

    
