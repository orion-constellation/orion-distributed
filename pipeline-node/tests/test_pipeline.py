def test_successful_message_delivery(self):
        class MockMessage:
            def topic(self):
                return "test_topic"
        
            def partition(self):
                return 0
    
        msg = MockMessage()
        err = None
        delivery_report(err, msg)
        
     # load a well-formed dictionary message
def test_load_well_formed_message(self):
    # Arrange
    transformed_message = {
        "key": "value",
        "another_key": "another_value"
    }
    expected_output = 'Loading message: {\n  "key": "value",\n  "another_key": "another_value"\n}'

    # Act
    with pytest.raises(SystemExit) as excinfo:
        load_message(transformed_message)

    # Assert
    assert excinfo.type == SystemExit
    assert excinfo.value.code == expected_output       
    
    
        # Transforms raw_message with all required fields into ECS format correctly
    def test_transforms_raw_message_with_all_required_fields(self):
        # Arrange
        raw_message = {
            '@timestamp': '2023-10-01T12:00:00Z',
            'event': {'category': 'threat', 'type': 'malware'},
            'threat': {'framework': 'MITRE ATT&CK', 'technique': 'T1059', 'id': 'T1059', 'name': 'Command and Scripting Interpreter'},
            'host': {'hostname': 'host1', 'ip': '192.168.1.1'}
        }
        expected_output = raw_message
    
        # Act
        result = ensure_ecs_format(raw_message)
    
        # Assert
        assert result == expected_output
        
        def test_failure_message(self):
        # Arrange
        err = Exception("Test error")
        msg = type('MockMessage', (object,), {'topic': lambda: 'test-topic', 'partition': lambda: 0})()
    
        # Act
        with pytest.raises(SystemExit) as excinfo:
            delivery_report(err, msg)
    
        # Assert
        assert excinfo.type == SystemExit
        assert excinfo.value.code == 1