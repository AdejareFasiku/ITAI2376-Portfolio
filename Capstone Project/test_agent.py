
"""
Comprehensive test suite for the Educational Process Automation Agent
Course: ITAI2376 - Capstone Project
Student: Adejare Fasiku
"""

import unittest
import sys
import os
# sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from datetime import datetime
from fn_code_adejarefasiku_fasiku_itai2376 import *

class TestEducationalAgent(unittest.TestCase):
    """Test suite for Educational Process Automation Agent"""
    
    def setUp(self):
        """Set up test fixtures"""
        self.agent = EducationalProcessAgent()
        self.test_student = StudentProfile(
            student_id="test_student_001",
            name="Test Student",
            level=StudentLevel.INTERMEDIATE,
            learning_style="visual",
            subjects=["mathematics", "physics"],
            performance_history=[0.8, 0.7, 0.9],
            engagement_score=0.75,
            last_active=datetime.now()
        )
    
    def test_agent_initialization(self):
        """Test agent initialization"""
        self.assertIsNotNone(self.agent)
        self.assertIsNotNone(self.agent.memory)
        self.assertIsNotNone(self.agent.safety)
        self.assertEqual(len(self.agent.tools), 4)
    
    def test_tool_integration(self):
        """Test external tool integrations"""
        # Test academic search
        search_result = self.agent.tools["academic_search"].search("machine learning")
        self.assertIn("results", search_result)
        
        # Test LMS integration
        lms_result = self.agent.tools["lms_integration"].get_student_data("student_001")
        self.assertTrue(lms_result["success"])
        
        # Test document processing
        doc_result = self.agent.tools["document_ai"].process_document("Test document")
        self.assertTrue(doc_result["success"])
        
        # Test content generation
        content_result = self.agent.tools["content_generator"].generate_content("quiz", "math")
        self.assertEqual(content_result["topic"], "math")
    
    def test_reasoning_patterns(self):
        """Test different reasoning patterns"""
        test_query = "Explain calculus concepts"
        
        # Test ReAct reasoning
        react_response = self.agent.process_request(test_query, reasoning_mode="react")
        self.assertEqual(react_response["reasoning_mode"], "react")
        
        # Test Chain-of-Thought reasoning
        cot_response = self.agent.process_request(test_query, reasoning_mode="cot")
        self.assertEqual(cot_response["reasoning_mode"], "chain_of_thought")
        
        # Test Planning reasoning
        planning_response = self.agent.process_request(test_query, reasoning_mode="planning")
        self.assertEqual(planning_response["reasoning_mode"], "planning")
    
    def test_memory_system(self):
        """Test memory storage and retrieval"""
        # Test episodic memory
        interaction = {"query": "test", "response": "test response", "topic": "math"}
        memory_id = self.agent.memory.store_episodic(interaction)
        self.assertIsNotNone(memory_id)
        
        # Test retrieval
        retrieved = self.agent.memory.retrieve_episodic("math")
        self.assertGreater(len(retrieved), 0)
    
    def test_safety_framework(self):
        """Test safety measures"""
        # Test input validation
        result = self.agent.safety.validate_input("What is calculus?")
        self.assertTrue(result["is_valid"])
        
        # Test malicious input
        malicious = "<script>alert('hack')</script>"
        result = self.agent.safety.validate_input(malicious)
        self.assertFalse(result["is_valid"])
    
    def test_rl_components(self):
        """Test reinforcement learning components"""
        # Test environment reset
        state = self.agent.rl_environment.reset(self.test_student)
        self.assertIn("student_level", state)
        
        # Test action execution
        action = {"type": "generate_content", "difficulty": "intermediate"}
        next_state, reward, done, info = self.agent.rl_environment.step(action)
        self.assertIsInstance(reward, float)

if __name__ == '__main__':
    unittest.main()
