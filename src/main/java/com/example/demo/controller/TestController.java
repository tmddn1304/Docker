package com.example.demo.controller;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.CrossOrigin;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
@CrossOrigin("*")
@RequestMapping("/")
public class TestController {
	
	
	
	@GetMapping("testvoew")
	public String test()
	{
		
		System.out.println("test");
		return "test";
		
		
		
	}

	
	
	
}
