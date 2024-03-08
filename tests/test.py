import pytest
from unittest.mock import Mock
from lambda_function import lambda_handler

class TestLambdaHandler:

    @pytest.mark.test 
    def test_lambda_handler_success(self):
        
        mock_table = Mock()
        mock_table.get_item.return_value = {'Item': {'views': 5}}
        mock_table.put_item.return_value = {}

        
        context = Mock()

        
        event = {}
        response = lambda_handler(event, context)

        #
        assert response['statusCode'] == 200
        assert response['body'] == '{"views": 6}'
        mock_table.put_item.assert_called_once_with(Item={'id': '0', 'views': 6})

    @pytest.mark.test 
    def test_lambda_handler_exception(self):
        
        mock_table = Mock()
        mock_table.get_item.side_effect = Exception("DynamoDB Error")

       
        context = Mock()

        
        event = {}
        response = lambda_handler(event, context)

    
        assert response['statusCode'] == 500
        assert 'error' in response['body']

