package order;


import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

import java.util.List;

@RestController
public class OrderController {

    private final MyOrderRepo orderRepo;

    @Autowired
    public OrderController(MyOrderRepo orderRepo) {
        this.orderRepo = orderRepo;
    }

    @GetMapping("/orders")
    public List<Order> list() {
        System.out.println(orderRepo.findAll());
        return orderRepo.findAll();
    }


}