#!/usr/bin/env python
# coding: utf-8

# In[2]:


def scale(data, factor):
    """Multiply all entries of numeric data list by the given factor."""
    for j in range(len(data)):
        data[j] *= factor


# In[3]:


def scale(data, factor):
    """Multiply all entries of numeric data list by the given factor"""
    
    # data = an instance of any mutable sequence type. List.
    # factor = a number that serves as the multiplicative factor for scaling.
    
    for j in range(len(data)):
        data[j] *= factor


# In[9]:


#Example: CreditCard Class.
class CreditCard:
    """A consumer credit card."""
    def __init__(self, customer, bank, acnt, limit):
        """Create a new credit card instance"""
        # The initial balance is zero.
        #customer = name of the customer.
        #bank = name of the bank.
        #acnt = account identifier.
        #limit = credit limit.
        self._customer = customer
        self._bank = bank
        self.account = acnt
        self._limit = limit
        self._balance = 0
        
    def get_customer(self):
        """Return name of the customer"""
        return self._customer
    def get_bank(self):
        "Return the bank's name"
        return self._bank
    def get_account(self):
        """Return the card identifying number typically"""
        return self._account
    def get_limit(self):
        """Return current credit limit"""
        return self._limit
    def get_balance(self):
        """Return current balance"""
        return self._balance
    def charge(self, price):
        """Charge given price to the card,
        assuming sufficient credit limit."""
        """Return True if charge was processed;
        False if charge was denied."""
        if price + self._balance > self._limit:
            return False
        else:
            self._balance += price
            return True
    def make_payment(self, amount):
        """Process customer payment that reduces balance."""
        self._balance -= amount

# A user can create an instance of the CreditCard class using a syntax as:
cc = CreditCard("Sam Fouad", "Ahly Bank", "5391 0375 9387 5309", 1000)
cc._customer


# In[11]:


if __name__ == "__main__":
    wallet = []
    wallet.append(CreditCard("Sam Fouad", "Alexandria Savings", "5391 0375 9387 5309", 1000))
    wallet.append(CreditCard("Sam Fouad", "Alexandria Fedral", "5391 0375 9387 5309", 1000))
    wallet.append(CreditCard("Sam Fouad", "Alexandria Finance", "5391 0375 9387 5309", 1000))

    for val in range(1, 17):
        wallet[0].charge(val)
        wallet[1].charge(2*val)
        wallet[2].charge(3*val)
    
    for c in range(3):
        print("Customer =", wallet[c].get_customer())
        print("Bank =", wallet[c].get_bank())
        print("Account =", wallet[c].get_account())
        print("Limit =", wallet[c].get_limit())
        print("Balance =", wallet[c].get_balance())
        while wallet[c].get_balance() > 100:
            wallet[c].make_payment(100)
            print("New Balance =", wallet[c].get_balance())
        print()


# In[13]:


class Vector:
    """Represents a vector in a multidimensional space."""
    
    def __init__(self, d):
        """Create d-dimensional vector of zeros."""
        self._coords = [0] * d
    def __len__(self):
        """Return the dimension of the vector."""
        return len(self._coords)
    def __getitem__(self, j):
        """Return jth coordinate of vector."""
        return self._coords[j]
    def __setitem__(self, j, val):
        """Set jth coordinate of vector to given value."""
        self._coords[j] = val
    def __add_(self, other):
        """Return sum of two vectors."""
        if len(self) != len(other):
            raise ValueError("Dimensions must agree.")
        result = Vector(len(self))
        for j in range(len(self)):
            result[j] = self[j] + other[j]
        return result
    
    def __eq__(self, other):
        """Return True if vector has some coordinates as other."""
        return self._coords == other_coords
    
    def __ne__(self, other):
        """Return True if vector differs from other"""
        return not self == other   #rely on existing __eq__ df.
    
    def __str__(self):
        """Produce string representation of vector."""
        return '<' + str(self._coords)[1:-1] + '>' #Adapt list representation.


# In[14]:


class SequenceIterator:
    """An iterator for any of Python's sequence types."""
    
    def __init__(self, sequence):
        """Create an iterator for the given sequence."""
        self._seq= sequence
        self._k = -1
    
    def __next__(self):
        """Return the next element, or else raise StopIteration error."""
        self._k += 1
        if self._k < len(self._seq):
            return(self._seq[self._k])
        else:
            raise StopIteration()
            
    def __iter__(self):
        """By convention, an iterator must return itself as an iterator"""
        return self


# In[15]:


class Range:
    """A class that mimic's the built-in range class."""
    
    def __init__(self, start, stop = None, step = 1):
        """Initialize a Range instance.
           Semantics is similar to built-in range class.
        """
        if step == 0:
            raise ValueError("step cannot be 0")
    
        if stop is None:
            start, stop = 0, start
    
    #calculate the effective length once.
        self._length = max(0, (stop - start + step - 1) // step)
    
    #need knowledge of start and step (but not stop) to support __getitem__
        self._start = start
        self._step = step
        
    def __len__(self):
        """Return number of entries in the range."""
        return self._length
    
    def __getitem__(self, k):
        """Return entry at index k (using std. interp. if negative)"""
        if k < 0:
            k += len(self)
        if not 0 <= k < self._length:
            raise IndexError("index out of range")
        return self._start + k * self._step


# In[16]:


class PredatoryCreditCard(CreditCard):
    """An extension to CreditCard that compounds interest and fees."""
    
    def __init__(self, customer, bank, acnt, limit, apr):
        """Create a new predatory credit card instance.
            The initial balance is zero.
            
            customer = the name of customer (i.e., Eslam)
            bank = bank's name: Ahly bank.
            acnt = account's identifier: 5391 0365 9387 3244
            limit = credit limit (measured in dollars)
            apr = annual percentage rate (0.234 for 23.4% APR)
        """
        super().__init__(customer, bank, acnt, limit) #call super constructor
        self._apr = apr
    def charge(self, price):
        """Charge given price to the card, assuming sufficient credit limit.
        Return True if charge was processed.
        Return False and assess $5 fee if charge is denied.
            """
        success = super().charge(price)
        if not success:
            self._balance += 5
        return success
    
    def process_month(self):
        """Assess monthly interest on outstanding balance."""
        if self._balance > 0:
            # if positive balance, convert APR to monthly multiplicative factor.
            monthly_factor = pow(1 + self._apr, 1 / 12)
            self._balance *= monthly_factor


# In[28]:


class Progression:
    """Iterator producing a generic progression.
        Default iterator produces the whole numbers: 0, 1, 2, ...
    """
    def __init__(self, start = 0):
        """Initialize current to the first value of the progression."""
        self._current = start
        
    def _advance(self):
        """Update self._current to a new value
        This should be overriden by a subclass to customize progression.
        By convention, if current is set to None, this designates the
        end of a finite progression.
        """
        self._current += 1
    def __next__(self):
        """Return the next element, or raise StopIteration error."""
        if self._current is None:
            raise StopIteration()
        else:
            answer = self._current
            self._advance()
            return answer
    def __iter__(self):
        """By convention, an iterator must return itself as an iterator."""
        return self
    
    def print_progression(self, n):
        """Print next n values of the progression."""
        print(' '.join(str(next(self)) for j in range(n)))


# In[29]:


class ArithmeticProgression(Progression):
    """Iterator producing an arithmetic progression."""
    
    def __init__(self, increment = 1, start = 0):
        """Create a new arithmetic progression.
        increment = the fixed constant to add to each term (default 1).
        start = the first term of the progression (default 0)
        """
        super().__init__(start)
        self._increment = increment
    
    def _advance(self):
        """Update current value by adding the fixed increment"""
        self._current += self._increment


# In[30]:


class GeometricProgression(Progression):
    """Iterator producing a geometric progression."""
    def __init__(self, base = 2, start = 1):
        """Create a new geometric progression.
        base: the fixed constant multiplied to each term (default 2)
        start: the first term of the progression (default 1)
        """
        super().__init__(start)
        self._base = base
    
    def _advance(self):
        """Update current value by multiplying it by the base value."""
        self._current *= self._base


# In[31]:


class FibonacciProgression(Progression):
    """Iterator producing a generalized Fibonacci progression."""
    def __init__(self, first = 0, second = 1):
        """Create a new fibonacci progression.
        first: the first term of the progression (default 0)
        second: the second term of the progression (default 1)
        """
        super().__init__(first)
        self._prev = second - first
    def _advance(self):
        """Update current value by taking sum of previous two."""
        self._prev, self._current = self._current, self._prev + self._current


# ### Testing progression.

# In[33]:


if __name__ == "__main__":
    
    print("Default progression: ")
    Progression().print_progression(10)
    
    print("Arithmetic Progression with increment 5: ")
    ArithmeticProgression(5).print_progression(10)
    
    print("Arithmetic progression with increment 5 and start 2: ")
    ArithmeticProgression(5, 2).print_progression(10)
    
    print("Geometric progression with base 3: ")
    GeometricProgression(3).print_progression(10)
    
    print("Fibonacci progression with default start values: ")
    FibonacciProgression().print_progression(10)
    
    print("Fibonacci progression with start values 4 and 6: ")
    FibonacciProgression(4, 6).print_progression(10)


# In[ ]:




