describe('My first test', function(0 {
   it('clicks the link "types"', function() {
      cy.visit('https://example.cypress.io') 
      cy.contains('type').click()
   })
})
