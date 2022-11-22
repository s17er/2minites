fn main() {
    for n in 0..10 {
      println!("{n}: Hello, Rust!");
    }

    let a = 10;
    let aref1 = &a;
    let aref2 = &a;
    println!("{}, {}, {}", a, aref1, aref2);

    let mut a = 10;
    let a_ref1 = &a;
    let a_mut_ref1 = &mut a;
    let a_mut_ref2 = &mut a;
    //*a_mut_ref1 = 20; // error.
    *a_mut_ref2 = 20;
    println!("{}", a);
    //println!("{}", a_ref1); // error.

}
