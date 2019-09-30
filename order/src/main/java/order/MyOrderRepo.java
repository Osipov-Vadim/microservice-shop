package order;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.repository.CrudRepository;

public interface MyOrderRepo extends JpaRepository<Order, Integer> {
}
